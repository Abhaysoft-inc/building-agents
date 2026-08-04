import { useState } from 'react'

const App = () => {
  const [prompt, setPrompt] = useState('')
  const [response, setResponse] = useState('')

  const handleSubmit = async () => {
    const apiResponse = await fetch('http://localhost:8000/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    })
    const data = await apiResponse.json()
    setResponse(typeof data === 'string' ? data : JSON.stringify(data, null, 2))
  }

  return (
    <div>
      <input
        type="text"
        name='prompt'
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
      <pre>{response}</pre>
    </div>
  )
}

export default App