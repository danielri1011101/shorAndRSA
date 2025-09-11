from qiskit_ibm_runtime import QiskitRuntimeService, Session
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.circuit.library import real_amplitudes
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Initialize session
service = QiskitRuntimeService()

# Prepare inputs
psi = real_amplitudes(num_qubits=2, reps=2)
H1 = SparsePauliOp.from_list([])
