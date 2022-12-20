import React, { useState, useEffect } from 'react'
import logo from './logo.svg'
import './App.css'
import axios from 'axios'
import PostList from './components/BackendJS'

function App() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        fetchData()
    }, [])

    const fetchData = () => {
        axios
            .get('http://127.0.0.1:8000/contacts')
            .then((res) => {
                setPosts(res.data)
            })
            .catch((err) => console.log(err))
    }

    return (
        <div>
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <PostList data={posts} />
            </header>
        </div>
    )
}

export default App
