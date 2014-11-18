from pprint import pprint
import linear_optics as lo

""" Test out the simulator """
data = [{"type":"bellpair","pos":{"x":-8,"y":0}},{"type":"sps","pos":{"x":-8,"y":5}},{"type":"crossing","pos":{"x":-7,"y":0}},{"type":"coupler","pos":{"x":-5,"y":1},"ratio":0.5},{"type":"crossing","pos":{"x":-3,"y":2}},{"type":"crossing","pos":{"x":-1,"y":4}},{"type":"bucket","pos":{"x":0,"y":0}},{"type":"bucket","pos":{"x":0,"y":2}},{"type":"bucket","pos":{"x":0,"y":4}}] 
pprint(data)

circuit = compile_circuit(data)

pprint(circuit)

circuit["patterns"]=list(it.combinations_with_replacement(range(circuit["nmodes"]), circuit["nphotons"]))

output_state = simulate(**circuit)

print "\nOutput state:"
for key, value in sorted(output_state.items(), key=lambda x:x[0]):
    if value>0: print key, "--", value

