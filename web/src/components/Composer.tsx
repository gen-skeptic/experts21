import { SendHorizontal, Square } from "lucide-react";
import { useState } from "react";

interface Props {
  busy: boolean;
  disabled: boolean;
  placeholder: string;
  onSend: (text: string) => void;
  onStop: () => void;
}

export function Composer({ busy, disabled, placeholder, onSend, onStop }: Props) {
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
        <span className="hint">Enter to send · Shift+Enter for a new line · every answer is billed to the site owner's Claude API key, so keep it short</span>
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
