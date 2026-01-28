"use client";

import ChatBox from "../components/ChatBox";
import useChat from "../hooks/useChat";

export default function HomePage() {
  const { messages, sendMessage, loading } = useChat();

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", padding: "1rem" }}>
      <h1 style={{ textAlign: "center" }}>📄 RAG Chat App</h1>

      <ChatBox
        messages={messages}
        onSend={sendMessage}
        loading={loading}
      />
    </div>
  );
}
