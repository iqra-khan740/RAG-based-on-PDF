"use client"

import type React from "react"

import { useRef, useState } from "react"
import { cn } from "@/lib/utils"
import { ChatBubble } from "./chat-bubble"

type Message = {
  id: string
  role: "user" | "bot"
  content: string
}

export function Chat({ baseUrl }: { baseUrl: string }) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: crypto.randomUUID(),
      role: "bot",
      content: "Hi! I’m your Book Brain assistant. Ask me anything about your books, notes, or highlights.",
    },
  ])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)
  const listRef = useRef<HTMLDivElement>(null)

  async function onSend(e: React.FormEvent) {
    e.preventDefault()
    const query = input.trim()
    if (!query || loading) return

    const userMsg: Message = { id: crypto.randomUUID(), role: "user", content: query }
    setMessages((prev) => [...prev, userMsg])
    setInput("")
    setLoading(true)

    try {
      const res = await fetch(`${baseUrl}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
        mode: "cors",
      })

      if (!res.ok) {
        throw new Error(`Request failed: ${res.status}`)
      }

      const data = (await res.json()) as { query: string; answer: string }
      const botMsg: Message = {
        id: crypto.randomUUID(),
        role: "bot",
        content: data.answer ?? "Sorry, I couldn’t find an answer.",
      }
      setMessages((prev) => [...prev, botMsg])
    } catch (err: unknown) {
      const botMsg: Message = {
        id: crypto.randomUUID(),
        role: "bot",
        content: "Oops! I couldn’t reach the server. Please check your BASE_URL or server status and try again.",
      }
      setMessages((prev) => [...prev, botMsg])
    } finally {
      setLoading(false)
      // scroll to bottom after a tick
      requestAnimationFrame(() => {
        listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: "smooth" })
      })
    }
  }

  return (
    <section className="flex h-[70dvh] flex-col">
      <div
        ref={listRef}
        className="relative flex-1 overflow-y-auto px-4 py-4 bg-background rounded-b-none rounded-t-xl overflow-hidden"
        aria-live="polite"
        aria-relevant="additions"
      >
        <img
          src="/images/green-sufi.jpg"
          alt=""
          aria-hidden="true"
          className="pointer-events-none select-none absolute inset-0 w-full h-full object-cover opacity-10 mix-blend-multiply"
        />

        <div className="space-y-3 relative z-10">
          {messages.map((m) => (
            <ChatBubble
              key={m.id}
              role={m.role}
              className={cn("soft-shadow", m.role === "user" ? "self-end" : "self-start")}
            >
              {m.content}
            </ChatBubble>
          ))}
          {loading && (
            <ChatBubble role="bot" className="opacity-90">
              Thinking…
            </ChatBubble>
          )}
        </div>
      </div>

      <form onSubmit={onSend} className="border-t border-border p-3">
        <div className="flex items-center gap-2">
          <label htmlFor="chat-input" className="sr-only">
            Type your question
          </label>
          <input
            id="chat-input"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about characters, chapters, or themes…"
            className="flex-1 rounded-lg px-3 py-2 input-surface outline-none"
            aria-label="Message input"
          />
          <button
            type="submit"
            disabled={loading || input.trim().length === 0}
            className={cn(
              "rounded-lg px-3 py-2 font-medium transition-colors soft-shadow",
              "bg-[var(--book-brand)] text-white hover:opacity-90 disabled:opacity-60",
            )}
          >
            Send
          </button>
        </div>
      </form>
    </section>
  )
}
