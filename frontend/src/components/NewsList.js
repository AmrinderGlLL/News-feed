import React from "react";

function NewsList({ articles }) {
  return (
    <ul>
      {articles.map((article, index) => (
        <li key={index}>
          <a href={article.url} target="_blank" rel="noopener noreferrer">
            {article.title}
          </a>
        </li>
      ))}
    </ul>
  );
}

export default NewsList;
