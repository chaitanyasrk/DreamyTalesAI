import React, { useState } from 'react';
import './Hobbies.css'; // Import CSS file for styling

const Hobbies = () => {
  const [hobby, setHobby] = useState('');
  const [generatedStory, setGeneratedStory] = useState('');

  const generateStory = () => {
    const story = "Once upon a time, there was a brave little dragon who loved to explore new places!";
    setGeneratedStory(story);
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
