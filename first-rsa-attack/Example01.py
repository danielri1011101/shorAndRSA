# Primitives within a session #

#
# Computation elements

# Import the Sampler primitive for running Qiskit
from qiskit_ibm_runtime import SamplerV2 as Sampler
# Same for the Estimator primitive
from qiskit_ibm_runtime import EstimatorV2 as Estimator
# Import the QiskitRuntimeService and Session classes
from qiskit_ibm_runtime import QiskitRuntimeService, Session
# Import the QiskitRuntimeService and Session classes
from qiskit_ibm_runtime import QiskitRuntimeService, Session
# Import the real_amplitudes circuit toolkit
from qiskit.circuit.library import real_amplitudes
# Import the registers and the circuit class
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
# Import the Pauli operator
from qiskit.quantum_info import SparsePauliOp
# From the compiler (transpiler), import the pass manager
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

#
# Constructing the job

myservice= QiskitRuntimeService()
# Get a wave function
psi= real_amplitudes(num_qubits=2, reps=2)
# Get a Hamiltonian
H1= SparsePauliOp.from_list( [("II", 1), ("IZ", 2), ("XI", 3)] )
# List argument theta
theta= [0, 1, 1, 2, 3, 5]
# Constructing the circuit
# Quantum register with two fields
qr= QuantumRegister(2, name= "qr")
# Classical register with two fields
cr= ClassicalRegister(2, name= "cr")
# The quantum circuit constructor recieves both registers as arguments
qc= QuantumCircuit(qr, cr, name= "may")
qc.h(qr[0])
qc.cx(qr[0], qr[1])
qc.measure(qr, cr)

#
# Job elements

mybackend= myservice.least_busy(operational= True, simulator= False)
# Get pass manager, which coerces ISA requirements on the circuit components
pm= generate_preset_pass_manager(target= mybackend.target, optimization_level= 1)

#
# Meet ISA requirements

may_isa= pm.run(qc)
psi_isa= pm.run(psi)
# Observables that are ISA
observables= H1.apply_layout(psi_isa.layout)

#
# Running job with Sampler

mysession= Session(backend= mybackend)
mysampler= Sampler(mode= mysession)
myjob= mysampler.run([may_isa])
myresult= myjob.result()[0]

#
# Running job with Estimator

myestimator= Estimator(mode= mysession)
myjob= myestimator.run([psi_isa, observables, theta])
myresult= myjob.result()[0]
