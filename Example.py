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

# Initialize the qiskit job, for later submission
myservice= QiskitRuntimeService()

# Get a wave function
psi= real_amplitudes(num_qubits=2, reps=2)

# Get a Hamiltonian
H1= SparsePauliOp.from_list( [("II", 1), ("IZ", 2), ("XI", 3)] )
theta= [0, 1, 1, 2, 3, 5]

# Create the quantum circuit
## Quantum register
qr= QuantumRegister(2, name="qr")
## Classical register
cr= ClassicalRegister(2, name="cr")
## Quantum circuit
qc= QuantumCircuit(qr, cr, name="may")
qc.measure(qr, cr)
