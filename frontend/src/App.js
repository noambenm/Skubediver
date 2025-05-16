// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import DiveLogForm from './components/DiveLogForm';
import DiveLogList from './components/DiveLogList';
import Calculator from './components/Calculator';

function App() {
  const [view, setView] = useState('logs');  // 'logs' or 'calculator'
  return (
    <div>
      <h1>Dive Log App</h1>
      <nav>
        <button onClick={() => setView('logs')}>Dive Logs</button>
        <button onClick={() => setView('calculator')}>Calculator</button>
      </nav>
      {view === 'logs' ? (
        <>
          <DiveLogForm />
          <DiveLogList />
        </>
      ) : (
        <Calculator />
      )}
    </div>
  );
}

export default App;
