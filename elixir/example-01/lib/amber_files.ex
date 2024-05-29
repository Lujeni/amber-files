defmodule AmberFiles do
  def increment_day_count([]), do: [1]
  def increment_day_count([h | t]), do: [1 + h | t]

  @doc """
  Splits the string into a list of uppercase letters.

  This is needed for form fields that don't offer a single input for the whole string,
  but instead require splitting the string into a predefined number of single-letter inputs.
  """
  @spec letters(String.t()) :: list(String.t())
  def letters(word) do
    word
    |> String.upcase()
    |> String.split("", trim: true)
  end

  @doc """
  Formats the address as an uppercase multiline string.
  """
  @type address_map :: %{street: String.t(), postal_code: String.t(), city: String.t()}
  @type address_tuple :: {street :: String.t(), postal_code :: String.t(), city :: String.t()}
  @type address :: address_map()| address_tuple()

  @spec format_address(address) :: String.t()
  def format_address(%{street: street, postal_code: postal_code, city: city}) do
    format_address({street, postal_code, city})
  end

  def format_address({street, postal_code, city}) do
    """
    #{String.upcase(street)}
    #{String.upcase(postal_code)} #{String.upcase(city)}
    """
  end

  def compare(_secret_number), do: "Make a guess"
  def compare(_secret_number, :no_guess), do: "Make a guess"
  def compare(secret_number, guess) when secret_number == guess, do: "Correct"

  def initials(full_name) do
    full_name
    |> String.split(" ")
    |> Enum.join(" ")
  end

  def to_milliliter({:cup, unit}) do {:milliliter, 240 * unit} end
  def to_milliliter({:fluid_ounce, unit}) do {:milliliter, 30 * unit} end

  def alert_recipient(level, legacy?) do
    # error
    case to_label(level, legacy?) do
      :unknown ->
        cond do
          legacy? == false -> :dev2
          true -> :dev1
        end
      :error ->
        :ops
      :fatal ->
        :ops
       _ ->
        false
    end
  end

  def lose?(power_pellet_active?, touching_ghost?) do
    (not power_pellet_active? and touching_ghost?)
  end

  def secret_xor(secret) do
    &(Bitwise.bxor(&1, secret))
  end
end
