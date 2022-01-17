from namespace import project

if __name__ == "__main__":
    dummy = project.Dummy()
    dummy.setVal(42)
    print(dummy.getVal())
    dummy = project.Dummy(42)
