import json
import os

class ReflectionAgent:
    def __init__(self, tree_path):
        """
        Initializes the agent by loading the JSON tree and setting up the state.
        """
        if not os.path.exists(tree_path):
            raise FileNotFoundError(f"Error: {tree_path} not found. Please ensure your JSON file is in the correct folder.")
            
        with open(tree_path, 'r') as f:
            self.tree = json.load(f)
            
        # State tracking for tallying signals (Internal vs External, etc.)
        self.state = {
            "axis1": {"internal": 0, "external": 0},
            "axis2": {"contribution": 0, "entitlement": 0},
            "axis3": {"altrocentric": 0, "selfcentric": 0}
        }
        # Dictionary to store exact user answers for interpolation
        self.answers = {}

    def get_node(self, node_id):
        """Helper to find a node by its ID."""
        return next((n for n in self.tree if n["id"] == node_id), None)

    def interpolate_text(self, text):
        """
        Replaces placeholders like {A1_OPEN.answer} with actual user choices 
        and {axisX.dominant} with the calculated dominant trait.
        """
        # Replace node-specific answer placeholders
        for node_id, answer in self.answers.items():
            placeholder = f"{{{node_id}.answer}}"
            if placeholder in text:
                text = text.replace(placeholder, str(answer))
        
        # Replace axis dominant trait placeholders
        for axis, counts in self.state.items():
            dominant = max(counts, key=counts.get)
            text = text.replace(f"{{{axis}.dominant}}", dominant)
        return text

    def find_next_child(self, parent_id):
        """Finds the next node in the sequence if no explicit jump is defined."""
        child = next((n for n in self.tree if n.get("parentId") == parent_id), None)
        return child["id"] if child else None

    def run(self):
        """Main loop to walk the tree."""
        current_id = "START"
        
        print("--- DT Daily Reflection Tree Agent ---")
        
        while current_id:
            node = self.get_node(current_id)
            if not node:
                break

            # 1. Update State if a signal is present
            if "signal" in node:
                axis_part, pole = node["signal"].split(":")
                if axis_part in self.state:
                    self.state[axis_part][pole] += 1

            # 2. Handle Display Logic based on Node Type
            if node["type"] in ["start", "bridge", "reflection", "summary"]:
                print(f"\n[SYSTEM]: {self.interpolate_text(node['text'])}")
                input("\n(Press Enter to continue...)")
                current_id = node.get("target") or self.find_next_child(current_id)

            elif node["type"] == "question":
                print(f"\n[QUESTION]: {self.interpolate_text(node['text'])}")
                options = node["options"].split("|")
                for i, opt in enumerate(options, 1):
                    print(f"  {i}. {opt}")
                
                try:
                    choice = int(input("\nSelect an option (number): ")) - 1
                    if 0 <= choice < len(options):
                        self.answers[node["id"]] = options[choice]
                        current_id = node.get("target") or self.find_next_child(current_id)
                    else:
                        print("Invalid choice, please try again.")
                except ValueError:
                    print("Please enter a valid number.")

            elif node["type"] == "decision":
                # Deterministic routing logic based on the last answer provided
                logic_parts = node["logic"].split(";")
                # Get the last answer recorded
                last_node_id = list(self.answers.keys())[-1]
                last_answer = self.answers[last_node_id]
                
                found_path = False
                for part in logic_parts:
                    condition, target = part.split(":")
                    allowed_answers = condition.split("=")[1].split("|")
                    
                    if any(ans.strip() in last_answer for ans in allowed_answers):
                        current_id = target
                        found_path = True
                        break
                
                if not found_path:
                    # Fallback to the next child if logic doesn't match
                    current_id = self.find_next_child(current_id)

            # 3. End of session
            if node["type"] == "end":
                print(f"\n[SYSTEM]: {node['text']}")
                break

if __name__ == "__main__":
    # Path assumes the script is run from the project root
    # Adjust "tree/reflection-tree.json" if your file name is different
    try:
        agent = ReflectionAgent("tree/reflection-tree.json")
        agent.run()
    except Exception as e:
        print(f"An error occurred: {e}")
