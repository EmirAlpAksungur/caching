
import './App.css';
import axios from 'axios'
import { useEffect } from 'react';

function App() {
  useEffect(()=>{
    axios.get('http://localhost:8000/api/recipes/').then((response)=>{
    console.log(response.data);
    })
  },[])
  const onClickHandler = (()=>{
    axios.delete('http://localhost:8000/api/recipes/1')
  })
  return (
    <div className="App">
      <button onClick={onClickHandler}>click</button>
    </div>
  );
}

export default App;
