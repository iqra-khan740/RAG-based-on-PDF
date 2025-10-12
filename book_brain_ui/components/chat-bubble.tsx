import type React from "react"
import { cn } from "@/lib/utils"

export function ChatBubble({
  role,
  className,
  children,
}: {
  role: "user" | "bot"
  className?: string
  children: React.ReactNode
}) {
  const bubbleClass = role === "user" ? "bubble-user" : "bubble-bot"

  return (
    <div
      className={cn("max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed", bubbleClass, className)}
      role="group"
      aria-roledescription={role === "user" ? "User message" : "Assistant message"}
    >
      {children}
    </div>
  )
}
