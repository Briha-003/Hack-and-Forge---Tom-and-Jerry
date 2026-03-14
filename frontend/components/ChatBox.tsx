"use client";

import { useState } from "react";
import { sendMessage } from "../lib/api";

export default function ChatBox(){

const [message,setMessage] = useState("");
const [chat,setChat] = useState<any[]>([]);

const handleSend = async ()=>{

const res = await sendMessage(message);

setChat([...chat,{user:message,ai:JSON.stringify(res)}]);
setMessage("");

};

return(
<div>

<input
value={message}
onChange={(e)=>setMessage(e.target.value)}
placeholder="Type your message"
/>

<button onClick={handleSend}>
Send
</button>

<div>

{chat.map((c,i)=>(
<div key={i}>
<p>User: {c.user}</p>
<p>AI: {c.ai}</p>
</div>
))}

</div>

</div>
)
}
