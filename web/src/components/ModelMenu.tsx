import type { Catalog, ModelChoice } from "../types";

export const money = (x: number) => (x < 0.1 ? `$${x.toFixed(3)}` : `$${x.toFixed(2)}`);

/** The model menu: Auto (the catalog's most cost-efficient model per task type), Claude only, or one model. */
export function ModelMenu({ catalog, value, onChange, disabled }: { catalog: Catalog; value: ModelChoice; onChange: (v: ModelChoice) => void; disabled?: boolean }) {
  const { providers } = catalog;
  const usable = (claude: boolean) => (claude ? providers.claude || providers.openrouter : providers.openrouter);
  const models = [...catalog.models].sort((a, b) => a.taskCost - b.taskCost);
  return (
    <label className="model-menu" title="Which model answers. Auto picks the most cost-efficient model for each task type (docs/model-catalog.md) and falls back to Claude.">
      <span>Model</span>
      <select value={value} onChange={(e) => onChange(e.target.value)} disabled={disabled}>
        <option value="auto">Auto: most cost-efficient per task</option>
        <option value="claude" disabled={!providers.claude && !providers.openrouter}>
          Claude: each expert's own brain
        </option>
        <optgroup label={`One model (cost per benchmark task pair, ${catalog.catalogDate})`}>
          {models.map((m) => (
            <option key={m.key} value={m.key} disabled={!usable(m.claude)}>
              {`${m.name} · ${money(m.taskCost)} · $${m.input}/$${m.output} per M${usable(m.claude) ? "" : " (needs OPENROUTER_API_KEY)"}`}
            </option>
          ))}
        </optgroup>
      </select>
    </label>
  );
}
