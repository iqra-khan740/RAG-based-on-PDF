import { NextResponse } from "next/server";

export async function POST(req) {
  const body = await req.json();

  const res = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      question: body.message, // 👈 VERY IMPORTANT
      top_k: 3,
    }),
  });

  const data = await res.json();

  return NextResponse.json({
    answer: data.answer, // 👈 pass ONLY answer
  });
}
