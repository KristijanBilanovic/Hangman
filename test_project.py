from project import init_dis, replace, output

def main():
    test_init_dis()
    test_replace()
    test_output()


def test_init_dis():
    assert init_dis("ja") == "__"
    assert init_dis("alarm") == "_____"
    assert init_dis("monster") == "_______"


def test_replace():
    assert replace("ALARM", "_____", "A") == "A_A__"
    assert replace("trash", "TR___", "h") == "TR__H"
    assert replace("APPLICATION", "_PPL_____ON", "i") == "_PPLI___ION"


def test_output():
    assert output("A_A__") == "A _ A _ _    ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  "
    assert output("TR__H") == "T R _ _ H    ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  "
    assert output("_PPLI___ION") == "_ P P L I _ _ _ I O N    ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  "


if __name__ == "__main__":
    main()
