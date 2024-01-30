import PropTypes from "prop-types";
import React from "react";
import { Label } from "semantic-ui-react";

const ExperimentLabel = ({ name, withKey }) => {
  return (
    <Label
      className="tiny navy"
      href={`/search?f=experiment:${name}`}
      {...(withKey && { key: name })}
    >
      {name}
    </Label>
  );
};

ExperimentLabel.propTypes = {
  name: PropTypes.string.isRequired,
  withKey: PropTypes.bool,
};

ExperimentLabel.defaultProps = {
  withKey: false,
};

const ListItemLabels = ({ metadata }) => {
  return (
    <>
      <Label
        className="tiny blue"
        href={`/search?f=type:${metadata.type.primary}`}
      >
        {metadata.type.primary}
      </Label>
      {metadata.type.secondary &&
        metadata.type.secondary.map((subtype) => (
          <Label
            key={subtype}
            className="tiny teal"
            href={`/search?f=type:${metadata.type.primary}%2Bsubtype:${subtype}`}
          >
            {subtype}
          </Label>
        ))}
      {metadata.categories?.primary && (
        <Label
          className="tiny dark-cyan"
          href={`/search?f=category:${metadata.categories.primary}`}
        >
          {metadata.categories.primary}
        </Label>
      )}
      {metadata.categories?.secondary &&
        metadata.categories.secondary.map((subcategory) => (
          <Label
            key={subcategory}
            className="tiny dark-green"
            href={`/search?f=category:${metadata.categories.primary}%2Bsubcategory:${subcategory}`}
          >
            {subcategory}
          </Label>
        ))}
      {metadata.tags &&
        metadata.tags.map((tag) => (
          <Label key={tag} className="tiny grey" href={`/search?f=tags:${tag}`}>
            {tag}
          </Label>
        ))}
      {metadata.experiment &&
          metadata.experiment.map(( exp ) => (
            <ExperimentLabel name={exp} />
          ))
      }
    </>
  );
};

export default ListItemLabels;
