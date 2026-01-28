 "use client";

import { useState } from "react";
import MessageBubble from "./MessageBubble";
import Loader from "./Loader";

export default function ChatBox({ messages = [], onSend, loading }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", padding: 20 }}>
      <h2>📘 RAG PDF Chat</h2>

      <div
        style={{
          border: "1px solid #ddd",
          minHeight: 300,
          padding: 10,
          marginBottom: 10,
          overflowY: "auto",
        }}
      >
        {messages.length === 0 && (
          <p style={{ color: "#999" }}>Ask something from your PDF…</p>
        )}

        {messages.map((msg, i) => (
          <MessageBubble key={i} role={msg.role} content={msg.content} />
        ))}

        {loading && <Loader />}
      </div>

      <div style={{ display: "flex", gap: 10 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question…"
          style={{ flex: 1, padding: 8 }}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}
