import type { Brain } from "../types";

export function BrainBadge({ alias, brains, effort }: { alias: string; brains: Record<string, Brain>; effort?: string }) {
  const brain = brains[alias];
  return (
    <span className={`brain brain-${alias}`} title={brain ? `${brain.family}: ${brain.strengths}` : alias}>
      {brain?.label ?? alias}
      {effort ? <span className="brain-effort">· {effort}</span> : null}
    </span>
  );
}
