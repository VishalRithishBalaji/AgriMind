from app.memory.memory_manager import memory_manager
from app.memory.chroma_store import chroma_store


def main():

    if chroma_store.count() > 0:

        print(
            f"Memory already contains {chroma_store.count()} cases."
        )

        return

    memory_manager.load_cases(
        "data/farming_cases.json"
    )

    print()

    print(
        f"Loaded {chroma_store.count()} farming cases into memory."
    )


if __name__ == "__main__":

    main()