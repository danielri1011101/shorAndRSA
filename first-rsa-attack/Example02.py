# For local testing #

#
# Backend components

# Import Qiskit Aer: backend whose instances permit local testing
from qiskit_aer import AerSimulator
# Import the real_amplitudes circuit toolkit
from qiskit.circuit.Qiskit Aer: backend import real_amplitudes
# We will again initialize the quantum circuit with a quantum register and a
# classical register
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
# Import the Pauli operator
from qiskit.quantum_info import SparsePauliOp
# Import pass manager
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

#
# Runtime tools

from qiskit_ibm_runtime import Session
from qiskit_ibm_runtime import SamplerV2 as Sampler
# Import fake provider
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

#
# Initialize quantum circuit

qc= QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()

#
# Running job locally with FakeManila

# Get fake provider
myfakeprov= FakeManilaV2()
# Get pass manager
pm= generate_preset_pass_manager(backend= myfakeprov, optimization_level= 1)
# Make qc meet isa requirements
isa_qc= pm.run(qc)
# Get the primitive
mysampler= Sampler(backend= myfakeprov)
# Run with Sampler primitive and get result
result= mysampler.run([isa_qc]).result()

#
# Running locally with AerSimulator
aer_sim= AerSimulator()
# Get passmanager with aer for backend
pm= generate_preset_pass_manager(backend= aer_sim, optimization_level= 1)
isa_qc= pm.run(qc)
# Session syntax supported but ignored
mysession= Session(backend= aer_sim)
sampler= Sampler(mode= session)
result= sampler.run([isa_qc]).result()
