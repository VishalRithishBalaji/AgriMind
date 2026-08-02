"""
==========================================================================
AgriMind

Module 5F Integration Test

Pipeline

Crop Knowledge
      ↓
Data Collection
      ↓
Context
      ↓
Planner
      ↓
Specialist Agents
      ↓
Collaborative Reasoning
      ↓
Executive Decision Intelligence
      ↓
Recommendation

==========================================================================
"""

from pprint import pprint

from app.orchestrator.dynamic_orchestrator import dynamic_orchestrator


###############################################################################
# Test Runner
###############################################################################

def run_test(

    crop,

    query,

    latitude=11.0168,

    longitude=76.9558

):

    print("\n")
    print("=" * 80)
    print(f"TESTING CROP : {crop.upper()}")
    print("=" * 80)

    result = dynamic_orchestrator.run(

        user_query=query,

        crop=crop,

        latitude=latitude,

        longitude=longitude

    )

    ###########################################################################
    # Crop Profile
    ###########################################################################

    print("\n")
    print("CROP PROFILE")
    print("-" * 80)

    pprint(result["crop_profile"])

    ###########################################################################
    # Context
    ###########################################################################

    print("\n")
    print("CONTEXT")
    print("-" * 80)

    pprint(result["context"])

    ###########################################################################
    # Planner
    ###########################################################################

    print("\n")
    print("EXECUTION PLAN")
    print("-" * 80)

    pprint(result["plan"])

    ###########################################################################
    # Specialists
    ###########################################################################

    print("\n")
    print("SPECIALIST OUTPUTS")
    print("-" * 80)

    for name, output in result["execution"]["specialists"].items():

        print("\n" + name)

        pprint(output)

    ###########################################################################
    # Collaborative Reasoning
    ###########################################################################

    print("\n")
    print("COLLABORATIVE REASONING")
    print("-" * 80)

    pprint(result["reasoning"])

    ###########################################################################
    # Executive Decision
    ###########################################################################

    print("\n")
    print("EXECUTIVE DECISION")
    print("-" * 80)

    pprint(result["executive"])

    ###########################################################################
    # Recommendation
    ###########################################################################

    print("\n")
    print("FINAL RECOMMENDATION")
    print("-" * 80)

    pprint(result["recommendation"])

    ###########################################################################
    # Statistics
    ###########################################################################

    print("\n")
    print("PIPELINE STATISTICS")
    print("-" * 80)

    pprint(result["execution"]["statistics"])

    ###########################################################################

    print("\nExecution Time:", result["total_time"], "seconds")


###############################################################################
# Main
###############################################################################

def main():

    run_test(

        crop="rice",

        query="Should I irrigate my rice crop today?"

    )

    run_test(

        crop="orange",

        query="How healthy is my orange plantation for the use of human?"

    )

    run_test(

        crop="apple",

        query="What should I do to maximize apple yield from the tree?"

    )


###############################################################################

if __name__ == "__main__":

    main()