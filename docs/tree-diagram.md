graph TD
    START(Start) --> A1_OPEN[Axis 1: Locus]
    A1_OPEN --> A1_D1{Decision}
    A1_D1 -- Productive --> A1_Q_VICTOR[Victor Path]
    A1_D1 -- Chaotic --> A1_Q_VICTIM[Victim Path]
    A1_Q_VICTOR --> BRIDGE1[Bridge 1-2]
    A1_Q_VICTIM --> BRIDGE1
    BRIDGE1 --> A2_OPEN[Axis 2: Orientation]
    %% Continue the flow for Axis 2 and 3
