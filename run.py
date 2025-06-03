import celpy
from celpy import celtypes

env = celpy.Environment(runner_class=celpy.InterpretedRunner)
ast = env.compile("dyn(this).b == 'foo'")
prog = env.program(ast)

bindings = {
    "this": celtypes.MapType({"a": "foo"})
}
result = prog.evaluate(bindings)
print("Result: {}".format(result))


# 0.2.0

# TypeError: no such overload: StringType('foo') <class 'celpy.celtypes.StringType'> != CELEvalError(*("no such member in mapping: 'b'", <class 'KeyError'>, None), tree='dyn(this).b') <class 'celpy.evaluation.CELEvalError'>


