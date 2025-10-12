"use client"

export const BASE_URL = "http://127.0.0.1:8000"

import { Chat } from "@/components/chat"

export default function Page() {

  
  return (
    <main className="min-h-screen bg-background flex items-center justify-center p-4">
      <div className="w-full max-w-2xl rounded-xl soft-shadow bg-card">
        <header className="px-4 py-4 border-b border-border bg-[var(--background)]">
          <div className="flex flex-col md:flex-row items-center md:items-start gap-4">
            <img
              src="/images/book-cover.jpg"
              alt="Book cover for 'The Forty Rules of Love'"
              className="w-28 h-auto rounded-md soft-shadow ring-1 ring-[color:var(--color-border)]"
            />
            <div className="text-center md:text-left">
              <h1 className="text-xl font-semibold text-balance">Book Brain — Forty Rules of Love Assistant</h1>
              <p className="text-sm text-muted-foreground">
                <span className="block">
                  {
                    '"The Forty Rules of Love" pairs a modern-day narrative with the 13th-century friendship of Rumi and Shams.'
                  }
                </span>
                <span className="block">
                  {
                    "It is a story of spiritual awakening where forty “rules” reveal a love that transcends fear, dogma, and ego."
                  }
                </span>
              </p>
              <div className="mt-2 inline-flex items-center gap-2">
                <span
                  className="text-xs font-medium px-2 py-1 rounded-full"
                  style={{
                    backgroundColor: "var(--book-accent-soft)",
                    color: "#07363a" /* teal-foreground for contrast */,
                  }}
                >
                  Based on the book
                </span>
                <span
                  className="text-xs font-medium px-2 py-1 rounded-full"
                  style={{
                    backgroundColor: "var(--book-brand)",
                    color: "#ffffff",
                  }}
                >
                  Chat about rules & stories
                </span>
              </div>
            </div>
          </div>
        </header>

        <Chat baseUrl={BASE_URL} />
      </div>
    </main>
  )
}
