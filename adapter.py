# Wraps a function and changes its output to uppercase
# Adds behavior without modifying original function

class OldPrinter:
    def print_text(self, msg):
        print(f"Old printer: {msg}")

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, msg):
        self.old_printer.print_text(msg)


printer = PrinterAdapter(OldPrinter())
printer.print("Hello from the adapter!")
