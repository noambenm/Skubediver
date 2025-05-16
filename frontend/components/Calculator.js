// frontend/src/components/Calculator.js
import React, { useState } from 'react';
const CALC_API = process.env.REACT_APP_CALC_API_URL;  // e.g., "http://localhost:5003"

function Calculator() {
  const [fo2, setFo2] = useState('0.32');       // fraction of O2 (e.g., 0.32 for 32%)
  const [depth, setDepth] = useState('30');     // depth in meters
  const [targetPO2, setTargetPO2] = useState('1.4'); // target PO2 in bar
  const [result, setResult] = useState('');

  const calculatePO2 = async () => {
    const res = await fetch(`${CALC_API}/calc/po2?fraction_o2=${fo2}&depth=${depth}`);
    const data = await res.json();
    setResult(`PO2 at ${depth}m with ${fo2} O2 = ${data.po2} bar`);
  };

  const calculateMOD = async () => {
    const res = await fetch(`${CALC_API}/calc/mod?fraction_o2=${fo2}&po2=${targetPO2}`);
    const data = await res.json();
    setResult(`MOD for PO2 ${targetPO2} bar with ${fo2} O2 = ${data.mod_meters} m`);
  };

  return (
    <div>
      <h2>PO<sub>2</sub> / MOD Calculator</h2>
      <div>
        <label>Fraction O2 (FO2):</label>
        <input value={fo2} onChange={e => setFo2(e.target.value)} />
      </div>
      <div>
        <label>Depth (m):</label>
        <input value={depth} onChange={e => setDepth(e.target.value)} />
        <button onClick={calculatePO2}>Calculate PO2</button>
      </div>
      <div>
        <label>Target PO2 (bar):</label>
        <input value={targetPO2} onChange={e => setTargetPO2(e.target.value)} />
        <button onClick={calculateMOD}>Calculate MOD</button>
      </div>
      {result && <p><strong>Result:</strong> {result}</p>}
    </div>
  );
}

export default Calculator;
