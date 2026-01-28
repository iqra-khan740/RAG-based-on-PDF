"use client";

import { useState } from "react";

export default function useChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text) => {
    if (!text) return;

    setLoading(true);

    // Add user message
    setMessages((prev) => [
      ...prev,
      { role: "user", content: text }
    ]);

    try {
      // Call backend
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: text }),
      });

      if (!res.ok) {
        throw new Error(`Error: ${res.status}`);
      }

      const data = await res.json();

      // Add assistant response
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.answer }
      ]);
    } catch (err) {
      console.error("Failed to fetch:", err);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Failed to get response from backend." }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return { messages, sendMessage, loading };
}
