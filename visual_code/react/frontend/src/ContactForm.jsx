import { useState } from "react";

const ContactForm = ({ }) => {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")


    return <form>
        <div>
            <label htmlFor="firstName">First Name:</label>
            <input 
                type="text" 
                id="firstName"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="lastName">Last Name:</label>
            <input 
                type="text" 
                id="lastName"
                value={firstName}
                onChange={(e) => setLastName(e.target.value)}
                
            />
        </div>
        <div>
            <label htmlFor="email">Email:</label>
            <input 
                type="text" 
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
        </div>
        <button type="submit">Create Contact</button>
    </form>

}