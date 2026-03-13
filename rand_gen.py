from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generator(n) -> str:
    qc = QuantumCircuit(7, 7)
    password = ""
    i=0
    while i<n:
        qc.h([0, 1, 2, 3, 4, 5, 6])
        qc.measure([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6])
        simulator = AerSimulator()
        job = simulator.run(qc, shots = 1)
        result = job.result()
        counts = result.get_counts()
        bitstring = list(counts.keys())[0]
        a=int(bitstring, 2)
        if a>=32 and a<128:
            password+= chr(a)
            i+=1 
    return password

if __name__ == "__main__":
    print("Random Password Generator using Qubits")
    n = int(input("How many characters in password: "))
    password = generator(n)
    print(f"Password Generated: {password}")