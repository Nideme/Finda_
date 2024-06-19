import React, { useState } from 'react';
import axios from 'axios';
import './ChatInterface.css';

const ChatInterface = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [googleSearch, setGoogleSearch] = useState(true);
    const [youtubeSearch, setYoutubeSearch] = useState(false);
    const [wikipediaSearch, setWikipediaSearch] = useState(false);

  const handleSend = async () => {
        if (input.trim()) {
            setMessages([...messages, { user: 'You', text: input }]);
            setInput('');
            try {
                const response = await axios.post('http://127.0.0.1:5000/chat', {
                    input,
                    google_search: googleSearch,
                    youtube_search: youtubeSearch,
                    wikipedia_search: wikipediaSearch,
                });
                const newMessages = [...messages, { user: 'You', text: input }, { user: 'Assistant', text: response.data.response }];
                // Update with search results
                const results = response.data.search_results;
                if (googleSearch) {
                    newMessages.push({ user: 'Google', text: formatResults(results.google) });
                }
                if (youtubeSearch) {
                    newMessages.push({ user: 'YouTube', text: formatResults(results.youtube) });
                }
                if (wikipediaSearch) {
                    newMessages.push({ user: 'Wikipedia', text: formatResults(results.wikipedia) });
                }
                setMessages(newMessages);
            } catch (error) {
                console.error('Error sending message:', error);
            }
        }
    };

    const formatResults = (results) => {
        return results.map(result => `${result.title}: ${result.link}`).join('\n');
    };

    

    return (
        <div className="chat-container">
            <input
                className="assistant-instructions"
                type="text"
                placeholder="Instructions for assistant"
            />
            <div className="chat-history">
                {messages.map((msg, index) => (
                    <div key={index} className="message">
                        <strong>{msg.user}:</strong> {msg.text}
                    </div>
                ))}
            </div>
            <div className="chat-input">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message here..."
                />
                <button onClick={handleSend}>Send</button>
            </div>
            <div className="search-options">
                <label>
                    <input
                        type="checkbox"
                        checked={googleSearch}
                        onChange={() => setGoogleSearch(!googleSearch)}
                    />
                    Google Search
                </label>
                <label>
                    <input
                        type="checkbox"
                        checked={youtubeSearch}
                        onChange={() => setYoutubeSearch(!youtubeSearch)}
                    />
                    YouTube Search
                </label>
                <label>
                    <input
                        type="checkbox"
                        checked={wikipediaSearch}
                        onChange={() => setWikipediaSearch(!wikipediaSearch)}
                    />
                    Wikipedia Search
                </label>
            </div>
        </div>
    );
};

export default ChatInterface;
