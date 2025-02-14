export function add(numbers?: string): number {
  let delimiter: string | RegExp = /[,\n]/;
  let input = numbers;
  
  if (numbers?.startsWith("//")) {
    [delimiter, input] = numbers.substring(2).split(/\n(.*)/);
  }

  return (
    input
      ?.split(delimiter)
      .map((n) => Number(n))
      .reduce((acc, current) => acc + current, 0) ?? 0
  );
}
