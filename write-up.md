Design Rationale: The Daily Reflection Tree
Candidate: Prince Sharma

Role: Fellowship Role Simulation (BA/DS)

1. The Core Philosophy: The "Mirror" Design
The fundamental goal of this tool is to act as a cognitive mirror for the employee. Unlike a traditional AI chatbot that provides generative (and often hallucinated) advice, this deterministic tree is designed to:

Neutralize Judgment: By providing fixed, non-moralizing options, the tool allows the user to self-identify their state without feeling "graded" by a machine.

Encourage Self-Discovery: By reflecting the user’s own choices back to them in the final summary, the tool facilitates "Aha!" moments where the user recognizes their own patterns of agency or entitlement.

Provide Consistency: Because the logic is deterministic, the user builds trust with the tool over time, knowing that the reflection quality depends entirely on their honesty, not a random seed.

2. Psychological Grounding
The tree is built upon three established psychological pillars, mapped across the required reflection axes:

Axis 1: Locus of Control (Julian Rotter) & Growth Mindset (Carol Dweck)
Internal vs. External: Questions are designed to distinguish between an "Internal Locus" (I am the driver) and an "External Locus" (I am a passenger).

The Design Choice: Instead of asking "Did you work hard?", I ask about the cause of the day's outcome. Attributing success to "Preparation" vs. "Luck" helps identify the user's mindset.

Axis 2: Organizational Citizenship Behavior (Organ, 1988)
Contribution vs. Entitlement: This axis tackles the hidden spectrum of "Psychological Entitlement."

The Design Choice: Questions focus on discretionary effort—actions taken that were not part of a formal job description. This helps the employee visualize their contribution to the team's ecosystem.

Axis 3: Self-Transcendence (Abraham Maslow, 1969)
Radius of Concern: This is the most advanced axis, moving the user from self-referential stress to a wider "Radius of Concern."

The Design Choice: By asking who benefited from the day’s work (Self vs. Team vs. End-User), the tree contextually shifts the user's focus toward "Altrocentrism," which is a proven reducer of workplace stress.

3. AI Collaboration & Guardrails
In designing this tree, I utilized Large Language Models (LLMs) as a collaborative power tool, not a primary author. My workflow included:

Option Generation: I used AI to brainstorm 4-5 diverse options for each question to ensure that every possible employee "persona" (from the tired overachiever to the frustrated newcomer) felt represented.

Human-in-the-loop (HITL): Every AI-generated question was manually edited to remove "moralizing" language. I disagreed with the AI's tendency to make "Victim" answers sound "bad," instead re-framing them as "natural reactions to stress."

Hallucination Control: By moving the AI’s output into a Deterministic JSON Tree, I created a permanent guardrail. The final product is "AI-Proof"—it cannot hallucinate because it only follows the hardcoded paths I have personally verified.

4. Future Improvements
Given more time, I would:

Sentiment-Aware Branching: Implement logic that tracks "cumulative state" more deeply to offer specialized "Bridge" nodes for users who consistently choose external locus options across several days.

Visual Analytics: Build a dashboard to visualize an employee's "Reflection Journey" over a month, showing their shift from Self-Centrism to Altrocentrism.
