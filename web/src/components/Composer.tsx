import { SendHorizontal, Square } from "lucide-react";
import { useState, type ReactNode } from "react";

interface Props {
  busy: boolean;
  disabled?: boolean;
  placeholder: string;
  /** Shown at the start of the bar under the text box (the model menu). */
  tools?: ReactNode;
  onSend: (text: string) => void;
  onStop: () => void;
}

export function Composer({ busy, disabled = false, placeholder, tools, onSend, onStop }: Props) {
  const [text, setText] = useState("");
  const submit = () => {
    const value = text.trim();
    if (!value || busy || disabled) return;
    onSend(value);
    setText("");
  };
  return (
    <form
      className="composer"
      onSubmit={(e) => {
        e.preventDefault();
        submit();
      }}
    >
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
            e.preventDefault();
            submit();
          }
        }}
        placeholder={placeholder}
        rows={3}
        maxLength={8000}
        aria-label="Message"
      />
      <div className="composer-bar">
        {tools}
        <span className="hint">Enter to send · Shift+Enter for a new line · answers are billed to the site owner's API keys</span>
        {busy ? (
          <button type="button" className="button button-secondary" onClick={onStop}>
            <Square size={14} aria-hidden /> Stop
          </button>
        ) : (
          <button type="submit" className="button button-primary" disabled={!text.trim() || disabled}>
            <SendHorizontal size={15} aria-hidden /> Send
          </button>
        )}
      </div>
    </form>
  );
}
