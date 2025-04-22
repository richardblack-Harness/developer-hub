import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import './DynamicMarkdownSelector.css';

export interface DynamicMarkdownSelectorProps {
  options: Record<string, string>;
}

const DynamicMarkdownSelector: React.FC<DynamicMarkdownSelectorProps> = ({ options }) => {
  const labels = Object.keys(options);
  const [selected, setSelected] = useState(labels[0]);
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    const fetchMarkdown = async () => {
      const path = options[selected];
      try {
        const response = await fetch(path);
        const text = await response.text();
        setMarkdown(text);
      } catch (e) {
        setMarkdown('Error loading content.');
      }
    };
    fetchMarkdown();
  }, [selected, options]);

  return (
    <div className="dynamic-markdown-selector">
      <hr className="selector-divider" />
      <div className="selector-tiles">
        {labels.map(label => (
          <button
            key={label}
            className={`selector-tile${selected === label ? ' selected' : ''}`}
            onClick={() => setSelected(label)}
            type="button"
          >
            {label}
          </button>
        ))}
      </div>
      <div className="markdown-content">
        <ReactMarkdown>{markdown}</ReactMarkdown>
      </div>
      <hr className="selector-divider" />
    </div>
  );
};

export default DynamicMarkdownSelector;
