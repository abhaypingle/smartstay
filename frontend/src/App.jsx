import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [properties, setProperties] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/properties')
      .then((response) => response.json())
      .then((data) => setProperties(data.properties))
      .catch((error) => console.error('Error fetching properties:', error))
  }, [])

  return (
    <div>
      <h1>SmartStay Properties</h1>
      {properties.map((property) => (
        <div key={property.id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
          <h3>{property.title}</h3>
          <p>City: {property.city}</p>
          <p>Rent: ₹{property.rent}/month</p>
        </div>
      ))}
    </div>
  )
}

export default App