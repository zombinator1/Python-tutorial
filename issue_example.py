class Runnable:  # (Protocol):
    def run(self) -> None: ...


class GoodPlugin:
    def run(self) -> None:
        print("Running correctly")


class BadPlugin:
    def execute(self) -> None:
        print("Oops — wrong method name")


def get_plugin(name: str) -> object:
    if name == "Good":
        return GoodPlugin()
    else:
        # mypy issue_example.py will detect this error
        return BadPlugin()


def start(plugin: Runnable):
    plugin.run()


plugin = get_plugin("Good")  # ← Everything is fine until you choose bad protocol
start(plugin)  # ← No crash... yet?
