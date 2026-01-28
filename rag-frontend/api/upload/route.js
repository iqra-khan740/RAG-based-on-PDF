import { NextResponse } from "next/server";

export async function POST() {
  // Later: send PDF to FastAPI backend
  return NextResponse.json({ status: "uploaded" });
}
