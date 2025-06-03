import celpy
from celpy import celtypes

env = celpy.Environment(runner_class=celpy.InterpretedRunner)

# Test field access
# Note that v0.2.0 raised the below error

# TypeError: no such overload: StringType('foo') <class 'celpy.celtypes.StringType'> != CELEvalError(*("no such member in mapping: 'b'", <class 'KeyError'>, None), tree='dyn(this).b') <class 'celpy.evaluation.CELEvalError'>

ast = env.compile("dyn(this).b == 'foo'")
prog = env.program(ast)

result = prog.evaluate({
    "this": celtypes.MapType({"a": "foo"})
})
print("Result: {}".format(result))

# Test has
ast = env.compile("has(this, 'b')")
prog = env.program(ast)

has_b = prog.evaluate({
    "this": celtypes.MapType({"a": "foo"})
})
print("Has b: {}".format(has_b))



