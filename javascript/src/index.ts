export function add(numbers?: string): number {
  let delimiter: string | RegExp = /[,\n]/;
  let input = numbers;

  if (numbers?.startsWith("//")) {
    [delimiter, input] = numbers.substring(2).split(/\n(.*)/);
  }

  const numberArray = input?.split(delimiter).map((n) => Number(n));

  if (!numberArray) {
    return 0;
  }

  for (let n of numberArray) {
    if (n < 0) {
      throw `negative numbers not allowed ${n}`;
    }
  }

  return numberArray?.reduce((acc, current) => acc + current, 0);
}
