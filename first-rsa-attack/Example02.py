from qiskit_aer import AerSimulator
# Again import the real_amplitudes circuit toolkit
from qiskit.circuit.library import real_amplitudes
# We will again initialize the quantum circuit with a quantum register and a
# classical register
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
# Import the Pauli operator
from qiskit.quantum_info import SparsePauliOp
