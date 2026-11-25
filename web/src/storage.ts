import type { ChatMessage } from "./types";

// Conversations stay in this browser only. Storage can be unavailable (private mode), so every access is guarded.
const PREFIX = "experts21:v1:";

export function loadConversation(key: string): ChatMessage[] {
  try {
    const raw = window.localStorage.getItem(PREFIX + "chat:" + key);
    const parsed = raw ? (JSON.parse(raw) as ChatMessage[]) : [];
    return Array.isArray(parsed) ? parsed.map((m) => ({ ...m, pending: false })) : [];
  } catch {
    return [];
  }
}

export function saveConversation(key: string, messages: ChatMessage[]): void {
  try {
    if (messages.length === 0) window.localStorage.removeItem(PREFIX + "chat:" + key);
    else window.localStorage.setItem(PREFIX + "chat:" + key, JSON.stringify(messages.slice(-60)));
  } catch {
    // storage full or blocked: the conversation still works for this visit
  }
}

/** The app password (only when the site owner set APP_PASSWORD), kept for this browser tab only. */
export function loadPassword(): string {
  try {
    return window.sessionStorage.getItem(PREFIX + "password") ?? "";
  } catch {
    return "";
  }
}

export function savePassword(password: string): void {
  try {
    if (password) window.sessionStorage.setItem(PREFIX + "password", password);
    else window.sessionStorage.removeItem(PREFIX + "password");
  } catch {
    // ignore
  }
}
