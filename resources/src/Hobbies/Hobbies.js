import React, { useState } from 'react';
import './Hobbies.css'; // Import CSS file for styling

const Hobbies = () => {
  const [hobby, setHobby] = useState('');
  const [generatedStory, setGeneratedStory] = useState('');

  const generateStory = () => {
    const url = "http://127.0.0.1:8000/talesapi/story/"; // Adjust this URL if your API is hosted elsewhere
    const request = {
      "kid_name" : "Arjun",
      "location" : "Bangalore, India",
      "age": 7,
      "hobbies" : hobby.split(',')
    };

    fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(request)
      })
      .then(response => response.json())
      .then(data => {
          // Assuming the story is returned under the 'story' key in the response
          const story = data.story;
          console.log('Received story:', story);
          setGeneratedStory(story);
      })
      .catch(error => {
          console.error('Error fetching story:', error);
      });
  };

  return (
    <div className="hobbies-container">
      <div className="hobbies-form">
        <h2>Enter Your Hobbies</h2>
        <input
          type="textArea"
          className="Hobbies-input"
          placeholder="Enter your hobby"
          value={hobby}
          onChange={(e) => setHobby(e.target.value)}
        />
        <button onClick={generateStory}>Generate Story</button>
        <div className="story-container">
          {generatedStory && <p>{generatedStory}</p>}
        </div>
      </div>
    </div>
  );
};

export default Hobbies;
