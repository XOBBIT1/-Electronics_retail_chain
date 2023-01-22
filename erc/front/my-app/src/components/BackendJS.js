import React, { useState } from 'react'
import Typical from 'react-typical'

const PostList = (props) => {
    console.log('Data', props.data)

    const { data } = props
    const [title, setTitle] = useState('COPY')

    return (
        <div>
            <Typical
                loop={Infinity}
                wrapper="b"
                steps={['Cleack for copy email', 100]}
            />
            <br />
            <button
                className="Cleack"
                onClick={() => {
                    data.map((item) => {
                        setTitle('COPIED')
                        navigator.clipboard.writeText(item.email)
                        return console.log('ok')
                    })
                }}
            >
                {title}
            </button>
        </div>
    )
}

export default PostList
