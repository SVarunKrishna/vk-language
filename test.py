from vk import vk


def test_conditional_exprs(cond_code, capsys):
    vk.exec(cond_code)
    out, err = capsys.readouterr()
    assert "x ( 15.0 ) is equal to 15!" in out.strip()


def test_logical_exprs(logic_code, capsys):
    vk.exec(logic_code)
    out, err = capsys.readouterr()
    assert "x != b:  True" in out.strip()


def test_math_exprs(math_code, capsys):
    vk.exec(math_code)
    out, err = capsys.readouterr()
    assert "modvar =  1.0" in out.strip()


def test_if(cond_code, capsys):
    vk.exec(cond_code)
    out, err = capsys.readouterr()
    assert "x ( 15.0 ) is equal to 15!" in out.strip()


def test_if_else(if_else_code, capsys):
    vk.exec(if_else_code)
    out, err = capsys.readouterr()
    assert "x ( 5.0 ) is less than 10!" in out.strip()


def test_for_loop(for_loop_code, capsys):
    vk.exec(for_loop_code)
    out, err = capsys.readouterr()
    assert "After loop: X = 14.0" in out.strip()


def test_while_loop(while_loop_code, capsys):
    vk.exec(while_loop_code)
    out, err = capsys.readouterr()
    assert "breaking out of loop..." in out.strip()


def test_function(fn_code, capsys):
    vk.exec(fn_code)
    out, err = capsys.readouterr()
    assert "Hello from myfunc_one!" in out.strip()


def test_function_return(fn_return_code, capsys):
    vk.exec(fn_return_code)
    out, err = capsys.readouterr()
    assert "Value returned from myfunc_one: 100.0" in out.strip()


def test_print(hello_world, capsys):
    vk.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_multi_print(multi_print, capsys):
    vk.exec(multi_print)
    out, err = capsys.readouterr()
    assert out.strip() == "5 + 5 = 10.0"


def test_exec(hello_world, capsys):
    vk.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_eval():
    out = vk.eval("5+5;")
    assert out == 10.0
  
