export function add(numbers?: string): number {
  return (
    numbers
      ?.split(/[,\n]/)
      .map((n) => Number(n))
      .reduce((acc, current) => acc + current, 0) ?? 0
  );
}
