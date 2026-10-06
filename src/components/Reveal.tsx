"use client";

import { motion } from "framer-motion";
import { ReactNode } from "react";

interface RevealProps {
  children: ReactNode;
  delay?: number;
  direction?: "up" | "down" | "left" | "right" | "none";
  className?: string;
  heavy?: boolean;
}

export default function Reveal({
  children,
  delay = 0,
  direction = "up",
  className = "",
  heavy = true,
}: RevealProps) {
  const directions = {
    up: { y: heavy ? 80 : 40, x: 0 },
    down: { y: heavy ? -80 : -40, x: 0 },
    left: { x: heavy ? 80 : 40, y: 0 },
    right: { x: heavy ? -80 : -40, y: 0 },
    none: { x: 0, y: 0 },
  };

  return (
    <motion.div
      className={className}
      initial={{
        ...directions[direction],
        opacity: 0,
        filter: heavy ? "blur(15px)" : "blur(0px)",
        scale: heavy ? 0.95 : 1,
      }}
      whileInView={{
        x: 0,
        y: 0,
        opacity: 1,
        filter: "blur(0px)",
        scale: 1,
      }}
      viewport={{ once: true, margin: "-100px" }}
      transition={{
        duration: 1.4,
        delay: delay,
        ease: [0.22, 1, 0.36, 1], // Smooth and slow ease
      }}
    >
      {children}
    </motion.div>
  );
}
