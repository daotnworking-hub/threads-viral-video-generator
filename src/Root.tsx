import React from "react";
import { ThreadsVideoComposition } from "./Composition";
import { ThreadsCommentReaderComposition } from "./ThreadsCommentReader";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <ThreadsCommentReaderComposition />
      <ThreadsVideoComposition />
    </>
  );
};
