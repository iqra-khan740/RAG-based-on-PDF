"use client";

export default function MessageBubble({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      style={{
        textAlign: isUser ? "right" : "left",
        margin: "8px 0",
      }}
    >
      <span
        style={{
          display: "inline-block",
          padding: "8px 12px",
          borderRadius: 10,
          background: isUser ? "#DCF8C6" : "#F1F1F1",
        }}
      >
        {content}
      </span>
    </div>
  );
}
