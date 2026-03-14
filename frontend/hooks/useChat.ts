import { useState } from "react"

export function useChat(){

const [messages,setMessages] = useState([])

const addMessage = (msg:any)=>{
setMessages([...messages,msg])
}

return {messages,addMessage}

}
